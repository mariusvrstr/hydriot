# Relay switch #
Relay switches allows you to switch on/off electronic devices that are externally powered

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/Relay%20Switch%20(Subaligu)/_resources/relay_switch.jpg)

In essence, you can modify a GPIO pin to be an output and then Low (3.3v) or High (5v). The relay switch interprits the changes to high as ON and low as OFF.

## Relay Configuration ##
In the bwlow configuration we are using [32/GPIO12] as the PIN. Very important for this relay switgh USE 3.3V NOT 5V, the LOW/HIGH distinction does not work if it is powered by 5V.

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/Relay%20Switch%20(Subaligu)/_resources/pi_connection.jpg)

## External Device Connection ##

![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/Relay%20Switch%20(Subaligu)/_resources/electrical_connection.jpg)

## Troubleshooting ##
You can test manually how the relay notifies you when it is on by (assuming 3 wire relay) by connecting the coms (Green) wire with the ground (black)


```console
python -m pip install RPi.GPIO
````
