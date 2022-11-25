import Control.Monad
import Data.Ratio
import Text.Printf


unit :: Ratio Integer
unit = 360 % 2 ^ 15

degree :: Integer -> Ratio Integer
degree n = (n % 1) * unit

mdu :: Integer -> Integer
mdu = fst . properFraction . (/0.06) . degree

mdu' :: Integer -> Integer
mdu' = round . (/0.06) . degree

bd :: Integer -> Integer
bd = flip div 100

md :: Integer -> Integer
md = flip mod 100 


file :: IO ()
file = do
  appendFile "Degree.txt" ("       Floor:            Round:            Degree:\n")  
  -- putStrLn  ("       Floor:            Round:            Degree:\n")  
  -- forM_ [1..32768] $ \x -> do
  forM_ [0..32768] $ \x -> do
    let y = mdu x
    let y' = mdu' x
    appendFile "Degree.txt" (printf "%5.d: %0.2d-%0.2d             %0.2d-%0.2d             %3.2f \n" x (bd y) (md y) (bd y') (md y') (fromIntegral x * (360 / 2 ^ 15) :: Double))  
    -- putStrLn (printf "%5.d: %0.2d-%0.2d             %0.2d-%0.2d             %3.2f \n" x (bd y) (md y) (bd y') (md y') (fromIntegral x * (360 / 2 ^ 15) :: Double))  
    
