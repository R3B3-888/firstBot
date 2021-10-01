import pypot.dynamixel as dyn

ports = dyn.get_available_ports()
if not ports:
    exit('No port')
dxl_io = dyn.DxlIO(ports[0])
dxl_io.disable_torque([5,2])
