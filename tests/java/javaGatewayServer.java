import py4j.GatewayServer;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class javaGatewayServer {
  public static void main(String[] args) {
    javaGatewayServer app = new javaGatewayServer();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
  }

  public String formatDate(String datetime, String pattern) {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
    LocalDate ldt = LocalDate.parse(datetime, formatter);
    return ldt.toString();
  }

    public String formatDateTime(String date, String pattern) {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
    LocalDateTime ldt = LocalDateTime.parse(date, formatter);
    return ldt.toString();
  }
}