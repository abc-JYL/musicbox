.delay 0.5
.async
    .play
        C4 E4 G4
    .end
    .await
.end
; Jingle Bell

.delay 0.25
.loop 2
    .loop 3
        .play
            E4 ; Jingle bells,
        .end
    .end
    .await
    .loop 3
        .play
            E4 ; Jingle bells,
        .end
    .end
    .await
    .play
        E4 G4 C4 D4 E4 ; Jingle all the way.
    .end
    .wait 0.75
    .loop 5
        .play
            F4 ; Oh what fun it is
        .end
    .end
    .play
        E4 E4 E4 E4 ; to ride in a
        E4 D4 D4 E4 D4 - G4 ; one horse open sleigh
    .end
    .await
.end

; Wait until the song finish.
.nodelay
.await
