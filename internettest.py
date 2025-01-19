import speedtest
import datetime

try:
    print("Initializing Speed Test...")
    st = speedtest.Speedtest()
    
    print("Fetching best server based on ping...")
    st.get_best_server()
    
    print("Performing download test...")
    download_speed = st.download()
    
    print("Performing upload test...")
    upload_speed = st.upload()
    
    ping = st.results.ping
    server = st.results.server
    
    # Convert speeds from bits per second to megabits per second
    download_mbps = download_speed / 1_000_000
    upload_mbps = upload_speed / 1_000_000
    
    print("\n--- Internet Speed Test Results ---")
    print(f"Timestamp: {datetime.datetime.now()}")
    print(f"Server: {server['name']} located in {server['country']}")
    print(f"Ping: {ping} ms")
    print(f"Download Speed: {download_mbps:.2f} Mbps")
    print(f"Upload Speed: {upload_mbps:.2f} Mbps")
    
except speedtest.ConfigRetrievalError:
    print("Error: Could not retrieve speedtest configuration.")
except speedtest.NoMatchedServers:
    print("Error: No matched servers. Please try again later.")
except speedtest.ServersRetrievalError:
    print("Error: Could not retrieve speedtest servers.")
except speedtest.SpeedtestException as e:
    print(f"Speedtest Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")