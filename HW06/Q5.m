deg_min = 0;
deg_max = 90;
deg_step = 0.1;

n_i = 1.5;
n_t = 1.0;

theta_deg = deg_min:deg_step:deg_max;
theta_i = deg2rad(theta_deg);

theta_t = asin(n_i * sin(theta_i) / n_t);

tm = 1 - (n_t .* cos(theta_i) - n_i .* cos(theta_t)) ./ ...
    (n_t .* cos(theta_i) + n_i .* cos(theta_t));

te = 1 - (n_i .* cos(theta_i) - n_t .* cos(theta_t)) ./ ...
    (n_i .* cos(theta_i) + n_t .* cos(theta_t));

figure(); hold on; grid on;
plot(theta_deg, abs(tm), 'k-');
plot(theta_deg, abs(te), 'b-');
legend('\Gamma_{TM}', '\Gamma_{TE}')
xlabel('Theta (degrees)')
ylabel('')
title('TE and TM Reflection Coefficients (n_i = 1.5; n_t = 1.0)')