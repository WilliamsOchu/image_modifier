#!/usr/bin/env python3

'''
This script will perform three basic actions based on user input
1. Rotate image
2. Resize image
3. Convert image format

'''

## Let us import our needed modules
import sys
import os
from PIL import Image



'''
The script enables a user to preprocess a single image or a bunch of images in a given directory

Simply run the script and provide the absolute path to the file or directory containing files to be preprocessed

For a single file conversion, the converted file is dropped in the parent folder
For a bulk conversion of a directory, you will need to state an output folder where the images will be converted into 
'''


def image_resize_single(abs_filepath):
	new_image = Image.open(abs_filepath)
	a = int(input("enter height: "))
	b = int(input("enter width: "))
	mode=(new_image.format)
	name_pick = abs_filepath.split(".", 1)
	new_image_name = name_pick[0] + "_resized" + "." + mode.lower()
	new_image = new_image.resize((a, b))
	new_image = new_image.save(new_image_name, mode.lower())
	sys.exit("\nConversion completed....!!")

def image_rotate_single(abs_filepath):
	new_image = Image.open(abs_filepath)
	angle_rotation = int(input("Rotate by how many degrees?: °"))
	mode=(new_image.format)
	name_pick = abs_filepath.split(".", 1)
	new_image_name = name_pick[0] + "_rotated" + "." + mode.lower()
	new_image = new_image.rotate(angle_rotation)
	new_image = new_image.save(new_image_name, mode.lower())
	sys.exit("\nConversion completed....!!")


def image_convert_single(abs_filepath):
	new_image = Image.open(abs_filepath)
	new_format = input("Enter the new image format: ")
	new_formated = new_format.lower()
	name_pick = abs_filepath.split(".", 1) 
	new_image_name = name_pick[0] + "." + new_formated
	if new_image.mode != 'RGB':
		new_image = new_image.convert('RGB')
		new_image = new_image.save(new_image_name, new_formated)
		sys.exit("\nConversion completed....!!")



def image_resize_bulk(abs_filepath):
	contents = os.listdir(abs_filepath)
	
	counts = 0
	a = int(input("enter height: "))
	b = int(input("enter width: "))
	output_directory = input("Enter the absolute path to a desired storage location: ")
	if not os.path.exists(output_directory):
		os.mkdir(output_directory)
	
		for items in contents:
			new_image_location = os.path.join(abs_filepath, items)

			new_image = Image.open(new_image_location)
			mode = new_image.format
			name_pick = items.split(".", 1)
			new_image_name = name_pick[0] + "_resized" + "." + mode.lower()
			new_image = new_image.resize((a, b))
			resized_image = os.path.join(output_directory, new_image_name)
			new_image = new_image.save(resized_image, mode.lower())
			counts +=1
			if counts == len(contents):
				sys.exit("\nConversion completed....!!")





def image_rotate_bulk(abs_filepath):
	contents = os.listdir(abs_filepath)
	
	counts = 0
	angle_rotation = int(input("Rotate by how many degrees?: °"))
	output_directory = input("Enter the absolute path to a desired storage location: ")
	if not os.path.exists(output_directory):
		os.mkdir(output_directory)
	

		for items in contents:
			new_image_location = os.path.join(abs_filepath, items)
			new_image = Image.open(new_image_location)
			mode = new_image.format
			name_pick = items.split(".", 1)
			new_image_name = name_pick[0] + "_rotated" + "." + mode.lower()
			new_image = new_image.rotate(angle_rotation)
			rotated_image = os.path.join(output_directory, new_image_name)
			new_image = new_image.save(rotated_image, mode.lower())
			counts +=1
			if counts == len(contents):
				sys.exit("\nConversion completed....!!")
			



def image_convert_bulk_(abs_filepath):
	contents = os.listdir(abs_filepath)
	counts = 0
	new_format = input("Enter the new image format: ")
	output_directory = input("Enter the absolute path to a desired storage location: ")
	if not os.path.exists(output_directory):
		os.mkdir(output_directory)

		for items in contents:
			new_image_location = os.path.join(abs_filepath, items)
			new_image = Image.open(new_image_location)
			new_formatted = new_format.lower()
			
			name_pick = items.split(".", 1)
			new_image_name = name_pick[0] + "." + new_formatted
		
			converted_image = os.path.join(output_directory, new_image_name)

			new_image = new_image.convert('RGB')
			new_image = new_image.save(converted_image, new_formatted)
			counts +=1
			if counts == len(contents):
				sys.exit("\nConversion completed....!!")
		





def single_selector():
	print("Select an option: \n1. Resize image \n2. Rotate image \n3. Convert image \nType \"exit\" to quit the program")
	selected_pick = input(":")
	if selected_pick == str(1):
		image_resize_single(abs_filepath)
	if selected_pick == str(2):
		image_rotate_single(abs_filepath)
	if selected_pick == str(3):
		image_convert_single(abs_filepath)
	if selected_pick.lower() == "exit":
		sys.exit("\nProgramme terminated....!!")	
	else:
		single_selector()





def bulk_selector():
	print("Select an option: \n1. Resize image \n2. Rotate image \n3. Convert image \nType \"exit\" to quit the program")
	selected_pick = input(":")
	if selected_pick == str(1):
		image_resize_bulk(abs_filepath)
	if selected_pick == str(2):
		image_rotate_bulk(abs_filepath)
	if selected_pick == str(3):
		image_convert_bulk_(abs_filepath)
	if selected_pick.lower() == "exit":
		sys.exit("\nProgramme terminated....!!")		
	else:
		bulk_selector()



abs_filepath = input("Enter the absolute filepath: ")
if not os.path.exists(abs_filepath):
	print("No such location exists  ... !! \nRenter a correct file or directory location")
	print("\n")
	reloader = sys.executable
	os.execl(reloader, reloader, * sys.argv)



if os.path.isfile(abs_filepath):
	single_selector()
else:
	bulk_selector()


