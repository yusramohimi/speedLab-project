import mysql.connector
import speedtest
import datetime
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


db_config = {
    'user': 'root',
    'password': '',  
    'host': 'localhost',
    'database': 'speedtest_db',
    'raise_on_warnings': True
}

class MySQLManager:
    def __init__(self, config):
        self.config = config
        self.init_db()

    def init_db(self):
        conn = mysql.connector.connect(**self.config)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                              id INT AUTO_INCREMENT PRIMARY KEY,
                              timestamp DATETIME,
                              download FLOAT,
                              upload FLOAT,
                              ping FLOAT
                          );''')
        conn.commit()
        cursor.close()
        conn.close()

    def save_results(self, results):
        conn = mysql.connector.connect(**self.config)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO results (timestamp, download, upload, ping)
                          VALUES (%s, %s, %s, %s)''',
                       (datetime.datetime.now(), results['download'], results['upload'], results['ping']))
        conn.commit()
        cursor.close()
        conn.close()

    def fetch_results(self):
        conn = mysql.connector.connect(**self.config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM results')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        df = pd.DataFrame(data, columns=['id', 'timestamp', 'download', 'upload', 'ping'])
        return df

class SpeedtestManager:
    def run_speed_test(self):
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()
        return results

class MatplotlibManager:
    def __init__(self):
        self.figure, self.ax = plt.subplots(figsize=(10, 6))

    def plot_results(self, df):
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        self.ax.clear()
        self.ax.plot(df['timestamp'], df['download'] / 1_000_000, label='Download (Mbps)', marker='o')
        self.ax.plot(df['timestamp'], df['upload'] / 1_000_000, label='Upload (Mbps)', marker='o')
        self.ax.plot(df['timestamp'], df['ping'], label='Ping (ms)', marker='o')
        self.ax.legend()
        self.ax.set_xlabel('Timestamp')
        self.ax.set_ylabel('Speed')
        self.figure.autofmt_xdate()

class TkinterManager:
    def __init__(self, root, db_manager, speedtest_manager, matplotlib_manager):
        self.root = root
        self.db_manager = db_manager
        self.speedtest_manager = speedtest_manager
        self.matplotlib_manager = matplotlib_manager
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="20", style="TFrame")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        style = ttk.Style()
        style.configure("TFrame", background="#2E3B4E")
        style.configure("TButton", font=("Helvetica", 16), background="#1C86EE", foreground="black")
        style.configure("TLabel", font=("Helvetica", 14), background="#2E3B4E", foreground="white")
        style.map("TButton", background=[("active", "#1C86EE"), ("disabled", "#A9A9A9")])

        run_button = ttk.Button(frame, text="Run Test", command=self.on_run_test, style="TButton")
        run_button.grid(row=0, column=0, pady=20, padx=20)

        self.download_label = ttk.Label(frame, text="Download: ", style="TLabel")
        self.download_label.grid(row=1, column=0, pady=10, padx=20, sticky=tk.W)
        self.upload_label = ttk.Label(frame, text="Upload: ", style="TLabel")
        self.upload_label.grid(row=2, column=0, pady=10, padx=20, sticky=tk.W)
        self.ping_label = ttk.Label(frame, text="Ping: ", style="TLabel")
        self.ping_label.grid(row=3, column=0, pady=10, padx=20, sticky=tk.W)

        self.canvas = FigureCanvasTkAgg(self.matplotlib_manager.figure, frame)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, pady=20, padx=20)

    def on_run_test(self):
        results = self.speedtest_manager.run_speed_test()
        self.db_manager.save_results(results)
        self.display_results(results)
        self.plot_results()

    def display_results(self, results):
        self.download_label.config(text=f"Download: {results['download'] / 1_000_000:.2f} Mbps")
        self.upload_label.config(text=f"Upload: {results['upload'] / 1_000_000:.2f} Mbps")
        self.ping_label.config(text=f"Ping: {results['ping']} ms")

    def plot_results(self):
        df = self.db_manager.fetch_results()
        self.matplotlib_manager.plot_results(df)
        self.canvas.draw()

def main():
    db_manager = MySQLManager(db_config)
    speedtest_manager = SpeedtestManager()
    matplotlib_manager = MatplotlibManager()

    root = ThemedTk(theme="arc")
    root.title("Speedtest")
    root.geometry("1200x800")

    app = TkinterManager(root, db_manager, speedtest_manager, matplotlib_manager)
    root.mainloop()

if __name__ == '__main__':
    main()
