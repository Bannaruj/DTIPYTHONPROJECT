stuID = input('ป้อน student ID: ')
stuName = input('ป้อน student Name: ')
stuBY = int(input('ป้อน student birth year: '))
print('--------------------------------------------------')
print(f"ยินดีต้อนรับ {stuID} {stuName} สู่ sau")
print(f"คุณเกิดปี {stuBY} เเปลว่าคุณอายุ {2023 - int(stuBY)} ปี")
print('--------------------------------------------------')
print("ยินดีต้อนรับ "+str(stuID)+' '+str(stuName)+' '+"สู่ sau")
print("คุณเกิดปี "+str(stuBY)+' '+"เเปลว่าคุณอายุ"+' '+str(2023 - int(stuBY))+' '+"ปี")
print('--------------------------------------------------')
print("ยินดีต้อนรับ",stuID,stuName,"สู่ sau")
print("คุณเกิดปี",stuBY,"เเปลว่าคุณอายุ",2023 - int(stuBY),"ปี")
print('--------------------------------------------------')
print("ยินดีต้อนรับ {0} {1} สู่ sau".format(stuID, stuName))
print("คุณเกิดปี {0}  เเปลว่าคุณอายุ {1}".format(stuBY,(2023 - stuBY)))
