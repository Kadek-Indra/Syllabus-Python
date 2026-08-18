names = ["Andi", "Budi", "Citra", "Deni", "Eka", "Fajar"]

math_scores = [85, 92, 78, 90, 88, 95]
english_scores = [80, 89, 85, 94, 87, 91]

zipped_math = zip(names, math_scores, english_scores)
average = lambda math, english: (math + english) / 2
sorted_average = sorted(zipped_math, key=lambda x: average(x[1], x[2]), reverse=True)

print("====Student Rankings====")
for name, math_score, english_score in sorted_average:
    print(f"{name:10}  - Average : {average(math_score, english_score):.2f}")