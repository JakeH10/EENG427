clc; close all; clear;

f = 600e6;

h_t = 10;
h_r = 10;
d = 26e3;

obs = [10 0; 20 100; 25 200; 30 250; 2 300];

h_n = [0; 0; 0];
v_Fn = [0; 0; 0];
L = [0; 0; 0];

for it = 2:4
    h_n(it-1) = obs(it,1) - obs(it-1,1) - obs(it,2) * (obs(it+1,1) - obs(it-1,1)) / (obs(it,2) + obs(it+1,2));
    v_Fn(it-1) = h_n(it-1) * sqrt(2 * (obs(it,2) + obs(it+1,2)) / ((3e8/f) * obs(it,2) * obs(it+1,2)));
    L(it-1) = 6.9 + 20*log10(sqrt((v_Fn(it-1) - 0.1)^2 + 1) + v_Fn(it-1) - 0.1);
end

L_tot = sum(L);