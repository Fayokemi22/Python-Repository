

menu = """
 List Of Menu Functions  
1. Phone Book
2. Messages 
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services

"""
print(menu)

phone_book = int(input("List Of Menu Functions  :"))

match phone_book:

	case 1:
		print("""
		1. Search
		2. Service Nos.
		3. Add name
		4. Erase
		5. Edit
		6. Assign tone
		7. Send b'card
		8. Options
		9. Speed dials
		10.Voice tags

		""")
		
		options = int(input("Phone Book Menu  :"))
		
		match options:

			case 8:
		
				print("""
			1. Type of views
			2. Memory status

			""")

	case 2:
		
		print("""

		Messages
		1. Write messages
		2. Inbox
		3. Outbox
		4. Picture messages
		5. Templates
		6. Smileys
		7. Message settings
		8. info service
		9. Voice mailbox number
		10. Service command editor 

		""")
	
		message = int(input("Message Menu "))
		
		match message:

			case 7:

				print("""
		
				 1. Set 1
 				 2.Common 
		
		 		""")
		
				message_settings = int(input("Message Settings :"))
				
				match message_settings:

					case 1:
						print("""

						1.Message Centre Number
						2.Message Sent As 
						3. Message Validity

					""")
							
					case 2:
						print("""

						1:Delivery Reports
						2.Reply Via Same Center
						3. Character Suppport

						""")

	case 4: 

		print("""

		Call register

		1. Missed calls
		2. Received calls
		3. Dialled numbers
		4. Erase recent call lists
		5. Show call duration
		6. Show call costs
		7. Call cost setting
		8. Prepaid credit

		""")
		
		show_call_duration = int(input("Show Call Duration :"))

		match show_call_duration:
						case 5:
							
							print("""
							1. Last call duration
							2. All calls' duration
							3. Received call duration
							4. Dialled call duration
							5. Clear timers

							""")		

						case 6:
						
							print("""
							1. Last call cost
							2. All calls' cost									3. Clear counters

							""")
						
						case 7: System.out.println("""

							1. Call cost limit
							2. Show costs in


							""")

	case 5:	

		print("""

		Tones

		1. Ringing tone
		2. Ringing volume
		3. incoming call alert
		4. Composer
		5. Message alert tone
		6. Keypad tones
		7. Warning and game tones
		8. Vibrating alert
		9. Screen saver
		""")

	case 6:
		print("""

		Settings

		1. Call Settings
		2. Phone Settings
		3. Security Settings
		4. Restore Factory ettings
	
		
		""")
	
		call_settings_menu = int(input("Call Settings Menu  :"))
		
		match call_settings_menu:
			case 1:
				print("""

				1. Authomatic redial
				2. Speed dialing
				3. Call waiting options
				4. Own number sending
				5. Phone line in use
				6. Automatic answer


				""")

				
			case 2:
					print("""

					1. Language
					2. Cell info display
					3. Welcome note
					4. Network selection
					5. Lights
					6. Confirm SIM service actions

					""")

			case 3:
				print("Security Settings Menu: ")
				print("""

				1. PIN code request
				2. Call barring service
				3. Fixed dialling
				4. Closed user group
				5. Phone security
				6. Change access codes
		
				""")

	case 7:

		print("""
		Call divert

		""")

	case 8:

		print("""
		Games
		
		""")

	case 9:

		print("""
		Calculator

		""")

	case 10:

		print("""
		Reminder

		""")

	case 11:

		print("""

		Clock

		1. Alarms Clock
		2. Clock Settings
		3. Date Setting
		4. Stopwatch
		5. Countdown timer
		6. Auto update of date and time


		""")

	case 12:

		print("""
		Profile
			
		""")

	case 13:

		print("""
		SIM Services

		""")





