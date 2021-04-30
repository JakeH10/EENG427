
%% Initialization
clear; clc;

%% Objects
brain  = struct('tissue', 'brain',...
                'mhz100',  struct('e_r', 68.47, 'conductivity', 0.44),...
                'mhz800',  struct('e_r', 46.25, 'conductivity', 0.73),...
                'mhz1000', struct('e_r', 45.43, 'conductivity', 0.80),...
                'mhz2000', struct('e_r', 43.21, 'conductivity', 1.26),...
                'mhz5000', struct('e_r', 39.30, 'conductivity', 3.48));
skull  = struct('tissue', 'skull',...
                'mhz100',  struct('e_r', 21.45, 'conductivity', 0.12),...
                'mhz800',  struct('e_r', 16.78, 'conductivity', 0.22),...
                'mhz1000', struct('e_r', 16.47, 'conductivity', 0.26),...
                'mhz2000', struct('e_r', 15.37, 'conductivity', 0.48),...
                'mhz5000', struct('e_r', 13.05, 'conductivity', 1.39));
muscle = struct('tissue', 'muscle',...
                'mhz100',  struct('e_r', 66.19, 'conductivity', 0.73),...
                'mhz800',  struct('e_r', 56.21, 'conductivity', 0.93),...
                'mhz1000', struct('e_r', 55.74, 'conductivity', 1.01),...
                'mhz2000', struct('e_r', 54.17, 'conductivity', 1.51),...
                'mhz5000', struct('e_r', 50.13, 'conductivity', 4.24));

%% Parameters
f_min =  100e6;
f_max = 5000e6;
f_step =   1e4;

f = f_min:f_step:f_max;

n = length(f);
d_p = zeros(3, n);

for i = 1:length(f)
      
    if f(i) < 450e6
        d_p(1, i) = penetration_depth(f(i),  brain.mhz100);
        d_p(2, i) = penetration_depth(f(i),  skull.mhz100);
        d_p(3, i) = penetration_depth(f(i), muscle.mhz100);
    elseif f(i) < 900e6
        d_p(1, i) = penetration_depth(f(i),  brain.mhz800);
        d_p(2, i) = penetration_depth(f(i),  skull.mhz800);
        d_p(3, i) = penetration_depth(f(i), muscle.mhz800);
    elseif f(i) < 1.5e9
        d_p(1, i) = penetration_depth(f(i),  brain.mhz1000);
        d_p(2, i) = penetration_depth(f(i),  skull.mhz1000);
        d_p(3, i) = penetration_depth(f(i), muscle.mhz1000);
    elseif f(i) < 3.5e9
        d_p(1, i) = penetration_depth(f(i),  brain.mhz2000);
        d_p(2, i) = penetration_depth(f(i),  skull.mhz2000);
        d_p(3, i) = penetration_depth(f(i), muscle.mhz2000);
    else
        d_p(1 ,i) = penetration_depth(f(i),  brain.mhz5000);
        d_p(2, i) = penetration_depth(f(i),  skull.mhz5000);
        d_p(3, i) = penetration_depth(f(i), muscle.mhz5000);
    end
end

figure(); hold on; grid on;
plot(f/1e6,d_p);
legend('brain', 'skull', 'muscle');
xlabel('frequency (MHz)');
ylabel('Penetration Depth (m)');
title('Penetration Depth of Multiple Tissues');