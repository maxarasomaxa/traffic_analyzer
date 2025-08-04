import pandas as pd
import matplotlib.pyplot as plt

def plot_traffic(packets):
	df=pd.DataFrame(packets)
	stats = df['src_ip'].value_counts().head(10)

	plt.figure(figsize=(10, 5))
	stats.plot(kind='bar', color ='skyblue')
	plt.title("Top-10 IP-addreses")
	plt.savefig('traffic_stats.png')
