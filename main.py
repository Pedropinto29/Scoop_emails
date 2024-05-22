import fetch_emails
import generate_rss
import subprocess

if __name__ == "__main__":
    email_addresses = fetch_emails.get_emails()
    
    rss_feed = generate_rss.generate_rss(email_addresses)

    with open ('emails.rss', 'w') as file:
        file.write(rss_feed.decode('utf-8'))

    try:
        subprocess.run(["git", "add", "emails.rss"], check=True)
        subprocess.run(["git", "commit", "-m", "Update emails.rss"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("emails.rss file has been updated and pushed to Github")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git commands: {e}")


