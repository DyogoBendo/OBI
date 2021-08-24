Program Batalha;

Const MaxN = 100;
      MaxM = 100;
      agua = '.';
      navio = '#';
      bomba = '*';
      visitado = 'o';

Var tabuleiro  : array[1..MaxN, 1..MaxM] of char;
    n, m, 
	i, j,
    k, navios,
    x, y       : integer;
	linha      : string[MaxM];

Procedure ImprimeTabuleiro;
var i, j : integer;
Begin
  For i := 1 To n Do Begin
    For j := 1 To m Do
      Write(tabuleiro[i,j]);
    WriteLn;
  End;
  WriteLn;
End;
	
Function Destruiu(x, y : integer): Boolean;
Var resposta : Boolean;
Begin
  resposta := True;
  If ((x > n) Or (x < 1) Or (y > m) Or (y < 1)) Then
    Resposta := True
  Else If (tabuleiro[x, y] = bomba) Then Begin
    tabuleiro[x, y] := visitado;
    resposta := Destruiu(x - 1, y) And resposta;
    resposta := Destruiu(x + 1, y) And resposta;
    resposta := Destruiu(x, y - 1) And resposta;
    resposta := Destruiu(x, y + 1) And resposta;
  End Else If (tabuleiro[x, y] = visitado) Then
    resposta := True
  Else If (tabuleiro[x, y] = agua) Then
    resposta := True
  Else
    resposta := False;
  Destruiu := resposta;
End;

Begin
  ReadLn(n, m);
  For i := 1 To n Do Begin
    ReadLn(linha);
	For j := 1 To m Do
	  tabuleiro[i,j] := linha[j];
  End;

  ReadLn(k);
  For i := 1 To k Do Begin
    ReadLn(x, y);
	If (tabuleiro[x, y] = navio) Then
	  tabuleiro[x, y] := bomba;
   End;

   navios := 0;
   For i := 1 To n Do
     For j := 1 To m Do
       If (tabuleiro[i, j] = bomba) Then
         If (Destruiu(i, j)) Then Begin
           Inc(navios);
           tabuleiro[i, j] := 'X';
         End;
    WriteLn(navios);
End.

  
