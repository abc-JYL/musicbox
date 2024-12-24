.delay 0.25

.sustain
.loop 2
    .play
        G4 A4 G4 F4 E4 F4 G4
        D4 E4 F4 E4 F4 G4
        G4 A4 G4 F4 E4 F4 G4
        D4 G4 E4 C4
    .end
    .await
    .play
        G4 A4 G4 F4 E4 F4 G4
        D4 E4 F4 E4 F4 G4
        G4 A4 G4 F4 E4 F4 G4
        D4 G4 E4 C4
    .end
    .await
.end

.nodelay
.await
