import pycurl_requests as requests


def write_good_token(Token, File):
    with open(File, "a") as file:
        file.write(f"{Token}\n")
        print("\033[92mGood Token\033[00m")


def check_token(Token, File, Good_File):
    headers = {"Authorization": Token, "User-agent": "Mozilla 5/0"}
    try:
        check_request = requests.get(
            "https://canary.discord.com/api/v9/users/@me", headers=headers
        )
        if check_request.status_code in range(200, 299):
            try:
                write_good_token(Token=Token, File=Good_File)
            except:
                print("\033[91mError Writing To File\033[00m")
        else:
            print("\033[91mBad Token\033[00m")
    except:
        print("\033[91mError During Request\033[00m")


def main(File, Good_File):
    with open(f"{File}", "r") as file:
        line = file.readline()
        for line in file:
            try:
                check_token(Token=line.strip(), File=File, Good_File=Good_File)
            except:
                print("\033[91mError\033[00m")


if __name__ == "__main__":
    File = input("\033[92mEnter Tokens File Name\033[00m: ")
    Good_File = input("\033[92mEnter Out File Name\033[00m: ")
    main(File=File, Good_File=Good_File)
