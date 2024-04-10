# lightblue_qrcode

import segno
qrcode = segno.make_qr("Allan is cooking omena")

qrcode.save("lightblue_qrcode.png",
            scale=5,
            border = 10,
            light = "lightblue",
            )
            