
      SUBROUTINE FIOOPN(UNIT, EVFILE)
      INTEGER UNIT
      CHARACTER*(*) EVFILE

C Open file for reading
      OPEN(UNIT, FILE=EVFILE, STATUS='UNKNOWN')

      END

      SUBROUTINE FIOOPNW(UNIT, EVFILE)
      INTEGER UNIT
      CHARACTER*(*) EVFILE

C Open file for writing. (Replace if already exists !)
      OPEN(UNIT, FILE=EVFILE, STATUS='REPLACE')

      END

      SUBROUTINE FIOCLS(UNIT)
      INTEGER UNIT

      CLOSE(UNIT)

      END
