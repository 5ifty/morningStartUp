@echo off

echo Running command now, please wait

echo Changing Sound Device to Sennheiser
nircmd.exe setdefaultsounddevice "Sennheiser" 1
echo Sound Device Changed

echo increasing system volume to "100"
nircmd.exe setsysvolume 65535
echo Volume is increased.

exit /B
