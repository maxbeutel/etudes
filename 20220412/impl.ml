
let rec dp1 v1 v2 =
	match (v1, v2) with
		 [], [] -> 0
		 | h1::t1, h2::t2 -> (h1 * h2) + ( dp1 t1 t2 )
		 | _ -> raise ( Failure "vectors must be of equal length" );;

let dp2 v1 v2 = 
        let rec aux v1 v2 q = 
                match (v1, v2) with
                        [], [] -> q
                        | h1::t1, h2::t2 -> aux t1 t2 ( q + h1 * h2)
                        | _ -> raise ( Failure "vectors must be of equal length" ) in
        aux v1 v2 0;;


dp1 [2; 3; 6] [1; 4; 5];; (* 44 *)

dp2 [2; 3; 6] [1; 4; 5];; (* 44 *)



let rec search needle haystack lo hi = 
        let mid = ( lo + hi ) / 2 in 
        if lo > hi then -1
        else if ( List.nth haystack mid ) = needle then mid
             else if ( List.nth haystack mid ) < needle then search needle haystack ( mid + 1) hi
             else search needle haystack lo ( mid - 1 ) 
;;

search 1 [1; 2; 3; 4; 5; 6; 7; 8; 9; 10] 0 9;;

