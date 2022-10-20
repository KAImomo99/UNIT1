# 1. 42 分 42 秒一共是多少秒？
s=42*60+42
print(s)
# 10 公里可以换算成多少英里？提示：一英里等于 1.61 公里
miles=10
yingli=1.61*miles
print(yingli)
#如果你花 42 分 42 秒跑完了 10 公里，你的平均配速是多少（每英里耗时，分别精确到分和秒）？你每小时平均跑了多少英里（英里/时）？
hours=s/3600
speed=yingli/hours
peisu=s/36000
print(speed,peisu)

