clear; close all; clc;

f = [900e6 1800e6];
v_r = 200e3;
v_t = 0;

c = 3e8;

f_d_max = [0 0];
T_c = [0 0];

for it = 1:length(f)
    l = c / f(it);
    
    f_d_max(it) = v_r / l;
    T_c(it) = 1 / f_d_max(it);
    
end