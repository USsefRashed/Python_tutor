#Dictionaries Like json or maps
#similar keys ----Lead to-->Runtime Error !!
ConvertMonth={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "lists":["kkkf","gfklka",True,145]
}
print(ConvertMonth["Jan"])#=
print(ConvertMonth.get("Feb"))
print(ConvertMonth.get("lists","The value is not exist"))#try here to enter random value
