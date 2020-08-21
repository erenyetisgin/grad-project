import random
import math
kat = 0;
lower = 0;
upper = 0;
lowervalue = 0;
uppervalue = 0;
value = 0;
cars = [] ;
one = [];
two = [];
three = [];
four = [];
rand1=random.randint(5,15);
rand2=random.randint(5,15);
rand3=random.randint(5,15);
rand4=random.randint(5,15);
print(rand1);
print(rand2);
print(rand3);
print(rand4);
cars.append(rand1);
cars.append(rand2);
cars.append(rand3);
cars.append(rand4);

if cars[0] % 5 == 0 and cars[0] > 5:
    kat = cars[0] / 5;
    one.append((7 * kat) - 3);
    one.append(2);
    one.append((7 * kat) - 3);
elif cars[0] <=  5:
    value = random.randint(3, 7);
    one.append(value);
    one.append(2);
    one.append(value);
else:
    lower = math.floor(cars[0] / 5)
    if int(lower) == 1:
        lowervalue = 7;

    upper = lower + 1;
    lowervalue = (7 * lower) - 3;
    uppervalue = (7 * upper) - 3;
    value = random.randint(lowervalue,uppervalue);
    one.append(value);
    one.append(2);
    one.append(value);
print("İlk Yol Kırmızı Işık Süresi",one[0]);
print("İlk Yol Sarı Işık Süresi",one[1]);
print("İlk Yol Yeşil Işık Süresi",one[2]);
if cars[1] % 5 == 0 and cars[1] > 5:
    kat = cars[1] / 5;
    two.append(one[2] + 2);
    two.append(2);
    two.append((7 * kat) - 3);
elif cars[1] <=  5:
    value = random.randint(3, 7);
    two.append(value);
    two.append(2);
    two.append(value);
else:
    lower = math.floor(cars[1] / 5);
    if int(lower) == 1:
        lowervalue = 7;
    upper = lower + 1;
    lowervalue = (7 * lower) - 3;
    uppervalue = (7 * upper) - 3;
    value = random.randint(lowervalue,uppervalue);
    two.append(one[2] + 2);
    two.append(2);
    two.append(value);
print("İkinci Yol Kırmızı Işık Süresi",two[0]);
print("İkinci Yol Sarı Işık Süresi",two[1]);
print("İkinci Yol Yeşil Işık Süresi",two[2]);
if cars[2] % 5 == 0 and cars[2] > 5:
    kat = cars[2] / 5;
    three.append(one[2] + two[2] + 4);
    three.append(2);
    three.append((7 * kat) - 3);
elif cars[2] <=  5:
    value = random.randint(3, 7);
    three.append(value);
    three.append(2);
    three.append(value);
else:
    lower = math.floor(cars[2] / 5);
    if int(lower) == 1:
        lowervalue = 7;
    upper = lower + 1;
    lowervalue = (7 * lower) - 3;
    uppervalue = (7 * upper) - 3;
    value = random.randint(lowervalue,uppervalue);
    three.append(one[2] + two[2] + 4);
    three.append(2);
    three.append(value);
print("Üçüncü Yol Kırmızı Işık Süresi",three[0]);
print("Üçüncü Yol Sarı Işık Süresi",three[1]);
print("Üçüncü Yol Yeşil Işık Süresi",three[2]);
if cars[3] % 5 == 0 and cars[3] > 5:
    kat = cars[3] / 5;
    four.append(one[2] + two[2] + three[2] + 6);
    four.append(2);
    four.append((7 * kat) - 3);
elif cars[3] <=  5:
    value = random.randint(3, 7);
    four.append(value);
    four.append(2);
    four.append(value);
else:
    lower = math.floor(cars[3] / 5);
    if int(lower) == 1:
        lowervalue = 7;
    upper = lower + 1;
    lowervalue = (7 * lower) - 3;
    uppervalue = (7 * upper) - 3;
    value = random.randint(lowervalue,uppervalue);
    four.append(one[2] + two[2] + three[2] + 6);
    four.append(2);
    four.append(value);
print("Dördüncü Yol Kırmızı Işık Süresi",four[0]);
print("Dördüncü Yol Sarı Işık Süresi",four[1]);
print("Dördüncü Yol Yeşil Işık Süresi",four[2]);



