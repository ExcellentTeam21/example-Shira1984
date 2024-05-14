import datetime
import random


def no_date(first, last):
    delta = (last - first).days
    random_days = random.randint(0, delta)
    random_date = first + datetime.timedelta(days=random_days)
    return random_date


def main():
    date_one = input("Please enter a date: ")
    date_two = input("Please enter another date: ")

    start_date = datetime.datetime.strptime(date_one, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(date_two, "%Y-%m-%d").date()

    random_date = no_date(start_date, end_date)

    if random_date.weekday() == 0:  # Monday is represented by 0
        print("I have no vinnaigrete!")
    else:
        print("Random date:", random_date)


if __name__ == "__main__":
    main()