## -*- mode: rpm-spec; -*-
##
## $Id: uisp.spec.in,v 1.3 2003/08/28 06:50:18 troth Exp $
##
## uisp.spec.  Generated from uisp.spec.in by configure.
##

%define debug_package %{nil}

%define uispVersion      20050207

Summary: Universal In-System Programmer for Atmel AVR and 8051.
Name: uisp
Version: %{uispVersion}
Release: 1
License: GPL
Group: Development/Tools
URL: http://freesoftware.fsf.org/download/uisp
Source: http://freesoftware.fsf.org/download/uisp/uisp-%{uispVersion}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-root

%description
Uisp is utility for downloading/uploading programs to AVR devices. Can also be
used for some Atmel 8051 type devices. In addition, uisp can erase the device,
write lock bits, verify and set the active segment.

For use with the following hardware to program the devices:
  pavr      http://avr.jpk.co.nz/pavr/pavr.html
  stk500    Atmel STK500
  dapa      Direct AVR Parallel Access
  stk200    Parallel Starter Kit STK200, STK300
  abb       Altera ByteBlasterMV Parallel Port Download Cable
  avrisp    Atmel AVR ISP (?)
  bsd       http://www.bsdhome.com/avrprog/ (parallel)
  fbprg     http://ln.com.ua/~real/avreal/adapters.html (parallel)
  dt006     http://www.dontronics.com/dt006.html (parallel)
  dasa      serial (RESET=RTS SCK=DTR MOSI=TXD MISO=CTS)
  dasa2     serial (RESET=!TXD SCK=RTS MOSI=DTR MISO=CTS)

	
%prep
%setup -q

%build

./configure --prefix=%{_prefix} --mandir=%{_mandir}

make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS CHANGES  CHANGES.old  COPYING  INSTALL  TODO kernel pavr
%{_prefix}/bin/uisp
%{_mandir}/man1/uisp.1.gz

%changelog
* Wed Aug 27 2003 Theodore A. Roth <troth@openavr.org>
- Add man page to package.
- Disable building of debug package.

* Sun May 26 2002 Theodore A. Roth <troth@openavr.org>
- Integrated in to build system.

* Sat Apr 20 2002 Theodore A. Roth <troth@openavr.org>
- Update to new 20020420 release.

* Fri Apr 18 2002 Theodore A. Roth <troth@openavr.org>
- Added patch to fix reading cal byte on tiny15. (from Alexander Popov)

* Mon Apr 08 2002 Theodore A. Roth <troth@openavr.org>
- Added patch to fix reading signature bytes.
- Added patch to fix some problems with srec uploading.

* Tue Mar 17 2002 Theodore A. Roth <troth@openavr.org>
- Added kernel/ and pavr/ directories to %doc files.

* Tue Mar 17 2002 Theodore A. Roth <troth@openavr.org>
- Initial spec file.
