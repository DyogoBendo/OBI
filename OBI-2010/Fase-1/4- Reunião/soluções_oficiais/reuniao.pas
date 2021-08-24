Program Reuniao;
Const Inf = 100000;
Var n, m : Integer;
    distancia : Array[1..100, 1..100] Of Integer;
    i, j, k, w: Integer;
    maior : Array[1..100] Of Integer;
    menor : Integer;

Procedure ImprimeDistancias;
Var i, j : Integer;
Begin
  For i := 1 To n Do Begin
    For j := 1 To n Do
      Write(distancia[i, j], '       ');
    WriteLn;
  End;
  WriteLn;
End;

Begin
  ReadLn(n, m);
  For i := 1 To n Do Begin
    maior[i] := 0;
    For j := 1 To n Do
      distancia[i, j] := Inf;
    distancia[i, i] := 0;
  End;

  For k := 1 To m Do Begin
    ReadLn(i, j, w);
    distancia[i + 1, j + 1] := w;
    distancia[j + 1, i + 1] := w;
  End;

  For k := 1 To n Do
    For i := 1 To n Do
      For j := 1 To n Do
        If (distancia[i, j] > (distancia[i, k] + distancia[k, j])) Then Begin
          distancia[i, j] := distancia[i, k] + distancia[k, j];
          distancia[j, i] := distancia[i, j];
        End;

  For i := 1 To n Do
    For j := 1 To n Do
      If (maior[i] < distancia[i, j]) Then
        maior[i] := distancia[i, j];

  menor := 1;
  For i := 2 To n Do
    If (maior[i] < maior[menor]) Then
      menor := i;

  WriteLn(maior[menor]);
end.
