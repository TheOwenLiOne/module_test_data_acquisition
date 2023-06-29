#include <A2D_DAQ.h>

#define NUM_CHANNELS 64  // Number of channels including 0-63

A2D_DAQ daq;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting A2D_DAQ 64CH Analog Read");

  daq.A2D_DAQ_init();
  
  for (int i = 0; i < NUM_CHANNELS; i++) {
    A2D_DAQ_channel_config ch_conf = daq.A2D_DAQ_get_default_config();
    ch_conf.channel_dir = A2D_DAQ_OUTPUT;
    ch_conf.channel_default_state = A2D_DAQ_HIGH;
    daq.A2D_DAQ_config_channel(i, ch_conf);
  }
  
  Serial.println("Setup Completed");
}

void loop() {
  for (int i = 0; i < NUM_CHANNELS; i++) {
    Serial.print("Channel");
    Serial.print(i);
    Serial.print(": ");
    Serial.println(daq.A2D_DAQ_get_analog(i));
  }

  delay(5000);
}
