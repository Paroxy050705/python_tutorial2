#break statement
students=["ram","shyam","kishan","radha","radhika"]
for s in students:
    if s=="radha":
        break;
    print(s)  #ram  shyam  kishan

#continue statement
fruit=["apple","mango","banana","guava","litchi"]
for f in fruit:
    if f=="banana":
        continue
    print(f)
# apple
# mango
# guava
# litchi   