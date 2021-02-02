% Author: Jacob Hoffer

clear; clc; close all;

load('q1.mat');

sig = getaudiodata(recObj);
sf = abs(fft(sig));

fs = recObj.SampleRate;
L = recObj.TotalSamples;

f = fs*(0:L)/L;


PSD = 10*log(sf.^2);

figure(); hold on; grid on;
plot(f(1:end-1), PSD, 'b');
plot(-f(1:end-1), flip(PSD), 'b');
xlabel("f (Hz)")
ylabel("PSD (dBm/Hz)")