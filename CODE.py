procedure insertionSort(books)
    for i ← 1 to length(books) - 1 do
        key ← books[i]
        j ← i - 1
        
        while j ≥ 0 and 
              (books[j].shelf > key.shelf OR
              (books[j].shelf = key.shelf AND books[j].order > key.order)) do
            books[j + 1] ← books[j]
            j ← j - 1
        end while
        
        books[j + 1] ← key
    end for
end procedure

