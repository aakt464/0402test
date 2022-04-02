#!/usr/bon/env python3
# -*- coding: utf-8 -*-

# import ui.mainWindow as win
# import database.sql as sql
from ui import mainWindow as win
from database import sql as sql


print("myTool Global")


def main():
	print("myTool LOCAL")

 # if __name__=='__main__':
 # 	#main()

	# win.main()
	# sql.main()
	# main()

import pprint
pprint.pprint(globals())

