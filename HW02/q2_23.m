% Author: Jacob Hoffer

SNR = -10:0.1:20;
B = [1e3, 1e4, 1e5, 1e6];

C = zeros(length(B),length(SNR));
for it = 1:length(B)
    C(it,:) = B(it)*log2(1+SNR);
end

figure(); hold on; grid on;
for it = 1:length(B)
    plot(SNR, real(C(it,:)));
end
legend(...
    "B = " + num2str(B(1)),...
    "B = " + num2str(B(2)),...
    "B = " + num2str(B(3)),...
    "B = " + num2str(B(4)));
xlabel("SNR (db)");
ylabel("C (bps)");
title("Channel capacity by SNR at four bandwidths")