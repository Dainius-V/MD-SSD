close all;
smd_303=load("ssd_303_30epochs.txt",'-ascii')'; 
smd_1004=load("ssd_1004_30epochs.txt",'-ascii')'; 
smd_3003=load("ssd_3003_30epochs.txt",'-ascii')'; 
figure();
plot(smd_303) ;
% title('SMD303 duomenu rinkinio patvirtinio nuostolis')
xlabel('Epocha');
ylabel('Nuostolis');

figure();
plot(smd_1004) ;
% title('SMD1004 duomenu rinkinio patvirtinio nuostolis')
xlabel('Epocha');
ylabel('Nuostolis');

figure();
plot(smd_3003) ;
% title('SMD3003 duomenu rinkinio patvirtinio nuostolis')
xlabel('Epocha');
ylabel('Nuostolis');