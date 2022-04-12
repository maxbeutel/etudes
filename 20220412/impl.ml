
let rec dp1 v1 v2 =
	match (v1, v2) with
		 [], [] -> 0
		| h1::t1, h2::t2 -> (h1 * h2) + ( dp1 t1 t2 )
		| _ -> raise ( Failure "vectors must be of equal length" );;

dp1 [2; 3; 6] [1; 4; 5];;
