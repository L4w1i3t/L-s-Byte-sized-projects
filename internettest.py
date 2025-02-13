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

    # Math to determine how good the internet speed is on avergage (scale of 1 to 10)
    # 1 is the worst and 10 is the best
    avg_speed = (download_mbps + upload_mbps) / 2
    speed_rating = 0
    if avg_speed < 1:
        speed_rating = 1
    elif avg_speed < 5:
        speed_rating = 2
    elif avg_speed < 10:
        speed_rating = 3
    elif avg_speed < 20:
        speed_rating = 4
    elif avg_speed < 50:
        speed_rating = 5
    elif avg_speed < 100:
        speed_rating = 6
    elif avg_speed < 200:
        speed_rating = 7
    elif avg_speed < 500:
        speed_rating = 8
    elif avg_speed < 1000:
        speed_rating = 9
    else:
        speed_rating = 10
    
    print("\n--- Internet Speed Test Results ---")
    print(f"Timestamp: {datetime.datetime.now()}")
    print(f"Server: {server['name']} located in {server['country']}")
    print(f"Ping: {ping} ms")
    print(f"Download Speed: {download_mbps:.2f} Mbps")
    print(f"Upload Speed: {upload_mbps:.2f} Mbps")
    print(f"Average Speed: {avg_speed:.2f} Mbps")
    print(f"Speed Rating: {speed_rating}/10")

    # User input to close the program
    input("\nPress Enter to exit...")
    
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