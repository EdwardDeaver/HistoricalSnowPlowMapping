source ../bin/activate
cd controller
nohup python streetDataControl.py &
nohup python getVehicleDataRunTime.py &

