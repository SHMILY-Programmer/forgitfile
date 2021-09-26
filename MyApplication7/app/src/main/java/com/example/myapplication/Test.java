package com.example.myapplication;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test {
    public void test(){
        // TODO Auto-generated method stub

        try {
//          Process proc = Runtime.getRuntime().exec("python C:\\file\\Speaker\\co_\\Include\\yuyinshibie.py");// 执行py文件
//            int pr=proc.waitFor();
//            BufferedReader isError = new BufferedReader(new InputStreamReader(proc.getErrorStream(),"gbk"));
//            String linee=null;
//            while ((linee=isError.readLine())!=null){
//                System.out.println(linee);
//            }
            //用输入输出流来截取结果
           String[] args1 = new String[] {"C:/file/Speaker/venv/Scripts/python.exe C:\\file\\Speaker\\co_\\Include\\yuyinshibie.py" };
//            Process proc = Runtime.getRuntime().exec( "cmd /c python3 "  + "C:\\file\\Speaker\\co_\\Include\\yuyinshibie.py" );
            Process proc = Runtime.getRuntime().exec(" C:/file/Speaker/venv/Scripts/python.exe C:\\file\\Speaker\\co_\\Include\\yuyinshibie.py");
//            int pr=proc.waitFor();
//            BufferedReader isError = new BufferedReader(new InputStreamReader(proc.getErrorStream(),"gbk"));
//            String linee=null;
//            while ((linee=isError.readLine())!=null){
//                System.out.println(linee);
//            }
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            proc.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


}