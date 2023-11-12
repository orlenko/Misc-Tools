on formatTwoDigits(value)
	return text -2 thru -1 of ("0" & value)
end formatTwoDigits

on run {input, parameters}
	set dt to (current date)
	set h to formatTwoDigits(hours of dt)
	set m to formatTwoDigits(minutes of dt)
	tell application "System Events"
		keystroke "["
		keystroke h
		keystroke ":"
		keystroke m
		keystroke "]\t"
	end tell
	--set thedate to (current date) as string
	--tell application "System Events"
	--	keystroke thedate
	--end tell
	
	return input
end run
