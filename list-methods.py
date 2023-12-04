numbers=[12,36,45,17,18,58,18]
letters=["a","u","m","t","c","n"]

val=min(numbers)
val=max(numbers)
val=min(letters)
val=max(letters)


val=numbers[3:6]
val=numbers[3:]
val=numbers[:4]

numbers[4]=40
numbers.append(49) #elemanları en sona ekler
numbers.append(78)
numbers.insert(2,11)  #istendiği index numarasından ekler
numbers.insert(-1,52)

# numbers.pop()    #en sondaki elemanı siler
# numbers.pop(0)  #içine girilen index numarasindaki değeri siler

# numbers.remove(49)   #silmek istediğiniz değeri içine yazıyorsunuz


numbers.sort()   #sayısal değerleri büyükten küçüğe doğru sıralar
numbers.reverse()  #tersten yazdırır

letters.sort()  #alfabetik sıraya göre yazdırır
letters.reverse()  #ters yazdırır
numbers.clear()  #bütün elemanaları siler

print(numbers)
print(letters)
print(len(numbers))
print(len(letters))

print(numbers.count(18))  #içine yazılan elemandan kaç tane olduğunu sayar