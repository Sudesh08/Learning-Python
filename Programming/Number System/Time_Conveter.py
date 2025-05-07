# Seconds to Hours, Minutes, Seconds
# Input seconds and convert it into hours, minutes, and seconds.

sec = int(input("Enter time is sec: "))


def convert_sec_to_hour_min_sec(second):
    r1=second%3600
    hour=int(second/3600)
    r2=r1%60
    minute=int(r1/60)
    return f"After converting {hour}h {minute}m {r2}s"

print(convert_sec_to_hour_min_sec(sec))
