module Main (main) where
import Control.Concurrent
import Text.Printf
import Control.Monad
import Data.Char (isDigit)
import Lib

main :: IO ()
main = 
  forever $ do
    s <- getLine
    forkIO $ setReminder s

setReminder :: String -> IO ()
setReminder s = do
  if any (isDigit) s then do
    let t = read s :: Int
    printf "ТАЙМЕР ЗАПУЩЕН НА %d мин\n" t
    threadDelay (60 * 10^6 * t)
    printf "СДЕЛАЙ ПЕРЕРЫВ. Окончен таймер на %d мин !! \BEL\n" t
  else return ()                              