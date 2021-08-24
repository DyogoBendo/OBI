program tesouro;

const MAXN = 100;
      MAXK = 100;
	
type TClue  = record x, y, d : longint end;
	
var N, K, npossibles,
     treasure_x, treasure_y : longint;
    clues                   : array [1..MAXK] of TClue;

procedure input;
var i : longint;
begin
	readln(N, K);
	for i := 1 to K do
		readln(clues[i].x, clues[i].y, clues[i].d)
end;

function matches(clue : TClue; x, y : longint) : boolean;
begin
	matches := abs(clue.x - x) + abs(clue.y - y) = clue.d
end;

procedure find_possibles;
var i, x, y  : longint;
    possible : boolean;
begin
	npossibles := 0;
	for x := 0 to N-1 do
		for y := 0 to N-1 do begin
			possible := true;
			for i := 1 to K do
				if not matches(clues[i], x, y) then
					possible := false;
			if possible then begin
				treasure_x := x;
				treasure_y := y;
				npossibles := npossibles + 1;
			end
		end
end;

procedure print_answer;
begin
	if npossibles = 1 then
		writeln(treasure_x, ' ', treasure_y)
	else
		writeln(-1, ' ', -1)
end;
	
begin
	input;
	find_possibles;
	print_answer;
end.
