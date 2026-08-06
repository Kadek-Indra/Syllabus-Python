def student_score(*args, **kwargs):
    print("====STUDENT INFORMATION====")
    for key, value in kwargs.items():
        print(f"{key:10} : {value}")

    print()

    print("==== SCORES ====")
    for score in args:
        print(score)

    print()

    total = sum(args)
    average = total / len(args)
    print(f"Average : {average}")


student_score(90, 85, 100, 75, name="Bangjon",
              class_name="X RPL 1",
              school="SMK TI DPS")