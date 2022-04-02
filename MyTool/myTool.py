#!/usr/bon/env python3
# -*- coding: utf-8 -*-

# import ui.mainWindow as win
# import database.sql as sql
from ui import mainWindow as win
from database import sql as sql


print("myTool Global")


def main():
	print("myTool LOCAL")


win.main()
sql.main()
main()

