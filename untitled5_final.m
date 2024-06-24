% dane wejściowe grafu

% polaczenie_a = [1 1 2 2 2 3 4];
% polaczenie_b = [2 4 3 4 5 5 5];
% wartosci = [6 1 5 2 2 5 1];
% xx = [0 5 9 0 5];
% yy = [5 5 2.5 0 0];

polaczenie_a = [1 1 2 2 3 4 5 6 7 7 8 9 9 10 10 10 12 12 13 13 15 15 17 17 19 20 20 21 22 23];
polaczenie_b = [2 9 3 6 4 5 6 7 8 9 24 10 12 11 12 15 13 16 14 15 16 17 18 19 20 21 22 23 23 24 ];
wartosci = [sqrt(10) sqrt(65) sqrt(5) sqrt(8) sqrt(12) 1 sqrt(10) sqrt(5) sqrt(10) sqrt(10) 13 sqrt(5) sqrt(7) sqrt(10) sqrt(34) sqrt(50) sqrt(13) sqrt(37) sqrt(5) 1 sqrt(41) sqrt(29) sqrt(13) sqrt(29) 5 1 sqrt(5) sqrt(10) 2 sqrt(26)];
xx = [0 3 1 2 2 5 7 8 8 7 8 12 14 15 14 18 19 22 21 18 19 16 16 21];
yy = [7 6 5 4 3 4 3 0 6 8 11 5 8 6 9 4 11 9 6 2 2 3 1 0];

poczatek =1; 

G = graph(polaczenie_a,polaczenie_b,wartosci);
figure(1)
plot(G,'XData',xx,'YData',yy,'EdgeLabel',G.Edges.Weight)

% zbiór wszystkich wierzchołków
Q = unique([polaczenie_a,polaczenie_b]); 

krok  = 1;
%nadanie nieskończonych kosztów dojścia do wszystkich punktów
odleglosc = inf*ones(1,length(Q));

%koszt dojścia do początku =0
odleglosc(poczatek) = 0; 

%nadanie nie istniejących poprzedników wszystkich punktów
poprzednik = nan*ones(1,length(Q)); 
poprzednik(poczatek) = 0; 

%CZĘŚĆ DLA PIERWSZEGO WIERZCHOŁKA

%jeśli są wyjścia z poczatku
if sum(polaczenie_a==poczatek)>0
    % wierzchołki z początku
    nastepne_punkty = polaczenie_b(polaczenie_a==poczatek); 
    % wartości ścieżek z oczątku
    odleglosc(nastepne_punkty) = wartosci(polaczenie_a==poczatek);
    % wcześniejszy wierzchołek, którego nie ma więc ustawiam na tą samą
    % wartość
    poprzednik(nastepne_punkty) = poczatek;
end
%jeśli są wejścia do poczatku
if sum(polaczenie_b==poczatek) >0
    nastepne_punkty = polaczenie_a(polaczenie_b==poczatek); 
    odleglosc(nastepne_punkty) = wartosci(polaczenie_b==poczatek);
    poprzednik(nastepne_punkty) = poczatek;
end

%zbiór przetworzonych wierzchołków
S = poczatek;

%tablica ze sprawdzonymi wierzcholkami
Wierzcholki{krok} = S;
%tablica z kosztami dojścia do konkretnych punktów
koszt_drogi{krok} = odleglosc;
%tablica poprzednich punktów
Poprzednicy{krok} = poprzednik;

%różnica Q i S, pozostałe wierzchołki
u  = setdiff(Q,S); 

% CZĘŚĆ DLA NASTĘPNYCH WIERZCHOŁKÓW

% while (~isempty(u))
while (u~=0)
    krok=krok+1;
    %najkrótsze ścieżki
    [M,I] =min(odleglosc(u)); 
    %wierzchołek do którego prowadzi najkrótsza ścieżka
    w=u(I); 
    %połączenie z początkiem
    S= [S,w]; 
    % wierzcholki do których jest połączenie z nowego (w)
    y = [polaczenie_b(polaczenie_a==w) , polaczenie_a(polaczenie_b==w)]; 
    y = unique(y);
    
    nastepne_punkty = setdiff(y,S); 
    
    for ctr=1:length(nastepne_punkty)
        
        filter = polaczenie_a==w & polaczenie_b==nastepne_punkty(ctr);
        if ~sum(filter) 
            filter = polaczenie_b==w & polaczenie_a==nastepne_punkty(ctr);
        end
        c_uv = wartosci(filter);
        if( odleglosc(w) + c_uv < odleglosc(nastepne_punkty(ctr)))
            poprzednik(nastepne_punkty(ctr)) = w;
        end
        odleglosc(nastepne_punkty(ctr))= min(odleglosc(nastepne_punkty(ctr)), odleglosc(w) + c_uv);
        
    end
    
 
    koszt_drogi{krok} = odleglosc;
    Poprzednicy{krok} = poprzednik;
    Wierzcholki{krok} = S;
  
    u  = setdiff(Q,S); 
end
ilosc_krokow = krok;


for ctr=1:ilosc_krokow
   fprintf('krok %d:\n',ctr)
   
   fprintf('Wierzcholki = [')
   fprintf('%g ' ,Wierzcholki{ctr})
   fprintf(']\n');
   
   fprintf('Koszt = [')
   fprintf('%g ' ,koszt_drogi{ctr})
   fprintf(']\n');
   
   
   fprintf('Poprzednik = [')
   fprintf('%g ' ,Poprzednicy{ctr})
   fprintf(']\n\n');
   
end


Koszty_calkowite = distances(G,poczatek,'Method','positive')
