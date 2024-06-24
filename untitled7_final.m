clear variables; clc;

coef=[130 -70 10.77 -22.33];
zakres=[-30 30];
szum=100000;
[x,y]=generuj_punkty(coef,zakres,szum);
Wejsciowe=[x;y];

IP=50;

a= -255 + 500*rand(IP,1);
b= -255 + 500*rand(IP,1);
c= -255 + 500*rand(IP,1);
d= -255 + 500*rand(IP,1);
e=zeros(IP,1);
coeff=[a b c d e];

coeff(1,:);
A=ocena_jakosci(Wejsciowe,coeff);
B=wylosuj(A,IP);
 rys_wykres(Wejsciowe,B);
 for i=1:10
    C=krzyzowanie(B);
    D=ocena_jakosci(Wejsciowe,C);
    E=wylosuj(D,IP);
    B=E;
  
     rys_wykres(Wejsciowe,B);
 end
 %B
 rys_wykres(Wejsciowe,B);
wybor_najblizszej(Wejsciowe,B);

function [x,y]=generuj_punkty(coef,zakres,szum)
x=zakres(1,1):1:zakres(1,2);
y=polyval(coef,x)+randn(1,length(x))*szum;
end


function wybor_najblizszej(wejsciowe,zbior)
     Wyniki=wzor(wejsciowe(1,:),zbior);
    n=length(Wyniki(:,1));
    min=inf;
    index=0;
    for i=1:n
           er(i,1) = immse(wejsciowe(2,:),Wyniki(i,:));
           if er(i,1)<min
               min=er(i,1);
               index=i;
           end
    end
    
    Napis=['Wspolczynniki to: a = ', num2str(zbior(index,1)),'   b = ',num2str(zbior(index,2)),'    c = ',num2str(zbior(index,3)),'    d = ',num2str(zbior(index,4)),'    error: ',num2str(min)];
    disp(Napis)
end

function A=ocena_jakosci(wejsciowe,zbior)
    Wyniki=wzor(wejsciowe(1,:),zbior);
    A=blad_sk(Wyniki,wejsciowe,zbior);
end

function A=krzyzowanie(zbior)
[B,Min]=zamiana_na_bin(zbior);
    C=random(B);
     A=zamiana_na_dec(C,Min);
end

function new=wylosuj(coef,ip)
        L=length(coef);
    R=randi([1,L],ip,1);
    for i=1:ip
        new(i,:)=coef(R(i),:);
        new(i,5)=0;
    end
end

function wyn=wzor(X,coef)
L=length(coef(:,1));
%K=length(X);
    for i=1:L
       % for j=1:K
        %wyn(i,j)=coef(i,1)*X(j).^3+coef(i,2)*X(j).^2+coef(i,3)*X(j)+coef(i,4);
        wyn(i,:)=polyval([coef(i,1) coef(i,2) coef(i,3) coef(i,4)],X);
        %end
    end
end

function [N,Min]=zamiana_na_bin(coef)
 Min= min(coef,[],'all');
%  if Min<0
    coef=(coef+abs(Min))*100;
%  else
%      coef=coef*100;
%  end
    for i=1:length(coef)
        for j=1:4
           N{i,j}=dec2bin(coef(i,j),16);
        end
    end
end

function N=zamiana_na_dec(coef,min)
     for i=1:length(coef)
        for j=1:4
           N(i,j)=bin2dec(coef{i,j});
        end
     end
%      if min<0
       N=N/100-abs(min);
%      else 
%          N=N/100;
%      end
end

function b=random(a)
    m=length(a);
    n=length(a{1});
    if (m>1)

      x=randi([10 n-1]);
     % x=13
         for k=1:4  
           for i=1:m
               for j=1:x
                 P{i,k}(j)=a{i,k}(j);
               end
               for j=x+1:n
                 R{i,k}(j)=a{i,k}(j) ;
                 R{i+1,k}(j)=a{1,k}(j);
               end 
           end          

                %b=a;
             for i=1:m
               for j=1:x
                   b{i+m,k}(j)=P{i,k}(j);
                 b{i,k}(j)=P{i,k}(j);
                end
               for j=x+1:n
                b{i+m,k}(j)=R{i,k}(j);
                 b{i,k}(j)=R{i+1,k}(j);
               end
             end
           end
    end
end

function new=blad_sk(wyn,Wejsc,coef)
% m=length(wyn(1,:));
n=length(wyn(:,1));
    for i=1:n
           er(i,1) = immse(Wejsc(2,:),wyn(i,:));
    end
 s=sum(er);
    for i=1:n
         coef(i,5)=floor(s./(er(i,1))./10);
    end
k=sum(coef(:,5));
a=0;
    for i=1:n
        if (coef(i,5))~=0
            for j=1:(coef(i,5))
                a=a+1; % moze lepiej i+j?
                new(a,:)=coef(i,:);
            end
        end
    end    
end

function rys_wykres(Wejsc,coef)
X=(Wejsc(1,1)-1):0.1:(Wejsc(1,length(Wejsc))+1);
Y=wzor(X,coef);
figure
plot(Wejsc(1,:),Wejsc(2,:),'k',X,Y)    
%y2=polyval([1 -1 1 1],x);
% legend('Wejsciowe','f1','f2','f3','f4','f5')
legend('Wejsciowe')
end


