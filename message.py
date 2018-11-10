from slackclient import SlackClient


def send_message(name):
    token = "your token"
    # found at https://api.slack.com/web#authentication

    sc = SlackClient(token)

    members = sc.api_call("users.list")["members"]
    for member in members:
        if member["name"] == name:
            member_id = member["id"]
            sc.api_call("chat.postMessage", channel=member_id,
                        text="Hi! It's time to clean our beautiful Coffee machine! No pain, no gain ;)")
            break


if __name__ == "__main__":
    send_message("daria.zakrevskaya")
