# DFRobot Gas Concentration Sensor

PX4 supports DFRobot "Gravity" range of gas sensors using the `dfrobot_gas` module.
This range includes electrochemical gas sensors for: O2, CO, H2S, NH3, H2, O3, SO2, NO2, HCL, CL2, HF and PH3.

::: tip
The driver was tested on hardware using a DFRobot Gravity H2 sensor.
It should support all sensor in the range, covering all the gases listed above.
:::

## Where to Buy {#store}

- [DFRobot](https://www.dfrobot.com/category-85.html)

## Hardware Setup

DFRobot Gravity electrochemical gas sensors can be connected to an unused _I2C port_.

::: info
The driver does not support using the sensors with a UART.
Some sensor models may require you to set the operating mode to I2C by flipping a physical switch.
:::

Build a cable following your board pinout and the DFRobot Gravity sensor pinout.
You will need to connect VCC, SDA, SCL and GND pins.

| Pin | DFRobot Gravity gas sensor |
| --- | -------------------------- |
| 1   | VCC                        |
| 2   | GND                        |
| 3   | SCL                        |
| 4   | SDA                        |

## Parameter Setup

The DFRobot gas sensor driver is not included in the default firmware for any board.
You must first add the driver to the firmware by enabling the following configuration option in the [PX4 Board Configuration (Kconfig)](../hardware/porting_guide_config.md#px4-menuconfig-setup):

```plain
CONFIG_DRIVERS_GAS_SENSOR_DFROBOT_GAS=y
```

After rebuilding and flashing the firmware, enable the DFRobot Gravity electrochemical gas sensor driver using the [`SENS_EN_DFGAS`](../advanced_config/parameter_reference.md#SENS_EN_DFGAS) parameter.

## Publishing

The gas concentration is published on the [SensorGasConcentration](../msg_docs/SensorGasConcentration) UORB topic by default.

## Further Information

- [DFRobot Gas sensor wiki](https://wiki.dfrobot.com/)
