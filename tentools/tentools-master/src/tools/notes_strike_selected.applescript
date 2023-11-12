

on chooseMenuItem2(theAppName, theMenuName, theMenuItemName, theMenuItemName2)
	try
		-- Bring the target app to the front
		tell application theAppName
			activate
		end tell
		
		-- Target the app
		tell application "System Events"
			tell process theAppName
				click menu item theMenuItemName2 of menu of menu item theMenuItemName of menu theMenuName of menu bar 1
			end tell
		end tell
		return true
	on error
		return false
	end try
end chooseMenuItem2

on run {input, parameters}
	chooseMenuItem2("Notes", "Format", "Font", "Strikethrough")
	return input
end run
